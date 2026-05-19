from common import ConfigMapSecretLoader


def test_ep06_env_from_merges_config_and_secret():
    pod = {'spec': {'containers': [{'envFrom': [{'configMapRef': {'name': 'app-config'}}, {'secretRef': {'name': 'app-secret'}}]}]}}
    env = ConfigMapSecretLoader().load_env(pod, {'app-config': {'LOG_LEVEL': 'info'}}, {'app-secret': {'DB_PASSWORD': 's3cret'}})
    assert env['LOG_LEVEL'] == 'info'
    assert env['DB_PASSWORD'] == 's3cret'
