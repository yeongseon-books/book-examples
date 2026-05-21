# Bad — 계정 존재 여부를 알려줌
if not user:
    return problem(404, "user.not_found", "User not found", "...")
if not check_password(user, password):
    return problem(401, "auth.wrong_password", "Wrong password", "...")

# Good — 동일한 응답으로 열거 공격 차단
return problem(401, "auth.invalid_credentials", "Invalid credentials",
               "이메일 또는 비밀번호가 올바르지 않습니다.")
