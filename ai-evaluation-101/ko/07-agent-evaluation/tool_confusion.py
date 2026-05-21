# agent_eval/tool_confusion.py
from sklearn.metrics import classification_report

# 100 test cases
expected_tools = ["send_email", "read_calendar", "send_email", ...]
actual_tools   = ["draft_email","read_calendar", "send_email", ...]

print(classification_report(expected_tools, actual_tools))
#                precision  recall  f1-score
# read_calendar      0.95    0.98    0.96
# send_email         0.85    0.70    0.77   ← often confused with draft_email
# draft_email        0.60    0.90    0.72
