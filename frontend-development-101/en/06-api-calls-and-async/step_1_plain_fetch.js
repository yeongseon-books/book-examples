async function loadUsers() {
  const res = await fetch("/api/users");
  return res.json();
}
