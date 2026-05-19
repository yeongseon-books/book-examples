from __future__ import annotations


def validate_oci_config(config: dict) -> list[str]:
    errors: list[str] = []
    process = config.get('process')
    root = config.get('root')
    mounts = config.get('mounts')

    if not isinstance(process, dict):
        errors.append('process is required')
    elif not isinstance(process.get('args'), list) or not process['args']:
        errors.append('process.args must be a non-empty list')

    if not isinstance(root, dict):
        errors.append('root is required')
    elif not root.get('path'):
        errors.append('root.path must be provided')

    if not isinstance(mounts, list) or not mounts:
        errors.append('mounts must be a non-empty list')
    else:
        for idx, mount in enumerate(mounts):
            if not isinstance(mount, dict):
                errors.append(f'mount {idx} must be an object')
                continue
            for key in ('destination', 'type', 'source'):
                if not mount.get(key):
                    errors.append(f'mount {idx} missing {key}')
    return errors
