import docker
import os
import time

def is_container_ready(container):
    container.reload()
    return container.status == "running"

def wait_for_stable_status(container, stable_duration=4, interval=1):
    stable_count = 0
    while stable_count < stable_duration:
        if is_container_ready(container):
            stable_count += interval
        else:
            stable_count = 0
        time.sleep(interval)
    return True

def start_database_container():
    client = docker.from_env()
    scripts_dir = os.path.abspath("./scripts")
    container_name = "database1"

    try:
        existing_container = client.containers.get(container_name)
        print(f"Container '{container_name}' exists. Stopping and removing...")
        existing_container.stop()
        existing_container.remove()
        print(f"{container_name} stopped and removed")
    except docker.errors.NotFound:
        print(f"Container '{container_name}' does not exist.")

    container_config = {
        "name": container_name,
        "image": "postgres:16.1-alpine3.19",
        "detach": True,
        "ports": {"5432/tcp": 5434},
        "environment": {
            "POSTGRES_USER": "postgres",
            "POSTGRES_PASSWORD": "postgres",
        },
        "volums" : [
            f"{scripts_dir}:/docker-entrypoint-initdb.d "
        ],
    }

    container = client.containers.run(**container_config)

    while not is_container_ready(container):
        time.sleep(5)

    if not wait_for_stable_status(container):
        raise RuntimeError("Container did not stabilize within the specified time.")

    return container