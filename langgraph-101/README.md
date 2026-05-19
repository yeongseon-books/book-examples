# langgraph-101

LangGraph 101 시리즈 예제 코드입니다.

- `ko/`: 한국어 프롬프트, 출력, 샘플 코퍼스
- `en/`: 동일한 그래프 로직의 영어 버전
- 모든 스텝은 독립 실행 가능합니다
- Tool-calling 예제는 `ChatGroq` + `ToolNode`를 사용합니다

## Requirements

```bash
pip install -r requirements.txt
export GROQ_API_KEY="your-groq-key"
```

## Series layout

```text
ko/01-graph-basics/step01_two_node_graph.py
ko/01-graph-basics/step02_three_node_pipeline.py
ko/02-state-and-checkpoints/step01_memorysaver_thread_state.py
ko/02-state-and-checkpoints/step02_multi_turn_memory.py
ko/03-conditional-edges/step01_router_function.py
ko/03-conditional-edges/step02_sentiment_branch_graph.py
ko/04-tool-calling-agent/step01_toolnode_with_chatgroq.py
ko/04-tool-calling-agent/step02_agent_loop.py
ko/05-multi-agent/step01_dual_agent_routing.py
ko/05-multi-agent/step02_supervisor_pattern.py
ko/06-langgraph-complete/step01_checkpoint_router_tools.py
ko/06-langgraph-complete/step02_streaming_pipeline.py

en/... (same structure with English strings)
```

## Notes

- All examples use `TypedDict` state.
- `model_dump()` is intentionally not used.
- `@tool` docstrings are preserved for tool selection.
- Tool-calling and streaming examples require `GROQ_API_KEY`.
