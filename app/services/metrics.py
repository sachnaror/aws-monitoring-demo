metrics_store = []


def record_metric(service, latency, status):

    metrics_store.append({
        "service": service,
        "latency": latency,
        "status": status
    })


def get_metrics():

    return metrics_store[-20:]
