# pytest + schemathesis로 contract test
import schemathesis

schema = schemathesis.from_uri("http://localhost:8000/openapi.json")

@schema.parametrize()
def test_api(case):
    response = case.call()
    case.validate_response(response)
