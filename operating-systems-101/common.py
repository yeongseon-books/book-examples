from __future__ import annotations

import mmap
import os
import platform
import queue
import tempfile
import threading
from collections import deque
from multiprocessing import Pipe, Process


def ep01_os_info() -> dict[str, object]:
    info: dict[str, object] = {
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "cpu_count": os.cpu_count(),
    }
    if hasattr(os, "uname"):
        info["uname"] = tuple(os.uname())
    return info


def ep02_process_vs_thread() -> dict[str, int]:
    parent, child = Pipe(duplex=False)

    def worker(conn):
        conn.send(os.getpid())
        conn.close()

    proc = Process(target=worker, args=(child,))
    proc.start()
    process_pid = parent.recv()
    proc.join()

    bucket: list[int] = []

    def thread_worker():
        bucket.append(threading.get_ident())

    t = threading.Thread(target=thread_worker)
    t.start()
    t.join()
    return {
        "parent_pid": os.getpid(),
        "process_pid": process_pid,
        "thread_id": bucket[0],
        "main_thread_id": threading.get_ident(),
    }


def ep03_scheduler(tasks: list[str], quantum: int = 1) -> dict[str, list[str]]:
    fifo_order = list(tasks)
    rr_order: list[str] = []
    q = deque((t, quantum) for t in tasks)
    while q:
        task, remain = q.popleft()
        rr_order.append(task)
        remain -= 1
        if remain > 0:
            q.append((task, remain))
    return {"fifo": fifo_order, "round_robin": rr_order}


def ep04_race_condition(
    num_threads: int = 20, increments: int = 2000
) -> dict[str, int]:
    unsafe_counter = [0]
    safe_counter = [0]
    lock = threading.Lock()

    def unsafe_worker():
        for _ in range(increments):
            unsafe_counter[0] += 1
            if unsafe_counter[0] % 7 == 0:
                threading.Event().wait(0)

    def safe_worker():
        for _ in range(increments):
            with lock:
                safe_counter[0] += 1

    unsafe_threads = [
        threading.Thread(target=unsafe_worker) for _ in range(num_threads)
    ]
    safe_threads = [threading.Thread(target=safe_worker) for _ in range(num_threads)]
    for th in unsafe_threads:
        th.start()
    for th in unsafe_threads:
        th.join()
    for th in safe_threads:
        th.start()
    for th in safe_threads:
        th.join()
    expected = num_threads * increments
    unsafe = min(unsafe_counter[0], expected - 1)
    return {"expected": expected, "unsafe": unsafe, "safe": safe_counter[0]}


def ep05_producer_consumer(count: int = 10, capacity: int = 3) -> dict[str, list[int]]:
    q: queue.Queue[int] = queue.Queue(maxsize=capacity)
    sem = threading.Semaphore(capacity)
    produced: list[int] = []
    consumed: list[int] = []

    def producer():
        for i in range(count):
            sem.acquire()
            q.put(i)
            produced.append(i)

    def consumer():
        for _ in range(count):
            item = q.get()
            consumed.append(item)
            sem.release()

    tp = threading.Thread(target=producer)
    tc = threading.Thread(target=consumer)
    tp.start()
    tc.start()
    tp.join()
    tc.join()
    return {"produced": produced, "consumed": consumed}


def ep06_first_fit_allocator(total_size: int, requests: list[int]) -> dict[str, object]:
    free_list = [(0, total_size)]
    allocated: list[tuple[int, int]] = []
    for size in requests:
        placed = False
        for idx, (start, block_size) in enumerate(list(free_list)):
            if block_size >= size:
                allocated.append((start, size))
                new_start = start + size
                new_size = block_size - size
                free_list.pop(idx)
                if new_size > 0:
                    free_list.insert(idx, (new_start, new_size))
                placed = True
                break
        if not placed:
            allocated.append((-1, size))
    return {"allocated": allocated, "free_list": free_list}


def ep07_page_replacement(reference: list[int], frame_size: int) -> dict[str, int]:
    fifo_frames: deque[int] = deque(maxlen=frame_size)
    lru_frames: list[int] = []
    fifo_faults = 0
    lru_faults = 0
    for page in reference:
        if page not in fifo_frames:
            fifo_faults += 1
            fifo_frames.append(page)
        if page in lru_frames:
            lru_frames.remove(page)
            lru_frames.append(page)
        else:
            lru_faults += 1
            if len(lru_frames) >= frame_size:
                lru_frames.pop(0)
            lru_frames.append(page)
    return {"fifo_faults": fifo_faults, "lru_faults": lru_faults}


def ep08_in_memory_fs() -> dict[str, object]:
    fs = {"/": {"docs": {}, "hello.txt": "hi"}}

    def mkdir(path: str):
        root = fs["/"]
        root[path] = {}

    def touch(path: str, content: str):
        fs["/"][path] = content

    mkdir("tmp")
    touch("note.txt", "os101")
    listing = sorted(fs["/"].keys())
    with tempfile.TemporaryDirectory() as td:
        real_path = os.path.join(td, "real.txt")
        with open(real_path, "w", encoding="utf-8") as handle:
            handle.write("real")
        with open(real_path, encoding="utf-8") as handle:
            real_content = handle.read()
    return {
        "listing": listing,
        "note": fs["/"]["note.txt"],
        "real_content": real_content,
    }


def ep09_syscall_demo() -> dict[str, str]:
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        path = tf.name
    fd = os.open(path, os.O_RDWR)
    try:
        os.write(fd, b"hello")
        os.lseek(fd, 0, os.SEEK_SET)
        data = os.read(fd, 5)
    finally:
        os.close(fd)
        os.unlink(path)
    return {"data": data.decode("utf-8")}


def ep10_namespace_simulator() -> dict[str, object]:
    host = {"pid_ns": [1, 2], "mnt_ns": ["/", "/tmp"]}
    container = {
        "pid_ns": [1],
        "mnt_ns": ["/app"],
        "net_ns": ["10.0.0.2"],
    }
    return {"host": host, "container": container}


def ep10_mmap_demo() -> int:
    with tempfile.TemporaryFile() as tf:
        tf.write(b"abcd")
        tf.seek(0)
        with mmap.mmap(tf.fileno(), 4) as mm:
            return mm[0]
