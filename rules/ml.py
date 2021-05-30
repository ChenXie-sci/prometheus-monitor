from prometheus_api_client import PrometheusConnect
import pandas as pd
import time

f1 = open('/home/ubuntu/prometheus-2.26.0.linux-amd64/rules/data.csv','w')

t1 = []
value = []
for i in range(3600):

    prom = PrometheusConnect(url ="http://localhost:9090", disable_ssl=True)

    t = (prom.custom_query(query="node_cpu_seconds_total")[0]['value'][0])
    cpu_idle = float(prom.custom_query(query="node_cpu_seconds_total")[0]['value'][1])

    cpu_used = float(prom.custom_query(query="node_cpu_seconds_total")[7]['value'][1])

    cpu_usage = (cpu_used / (cpu_used + cpu_idle))
    t1.append(t)
    value.append(cpu_usage)
    time.sleep(1)

dataframe = pd.DataFrame({'time':t1,'cpuusage':value})
dataframe.to_csv("data.csv",index=False,sep=',')
