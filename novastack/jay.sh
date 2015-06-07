PID=$(ps -ef | grep nova-scheduler | grep python | awk {'print$2'} | head -n 1)
 
if ! KEY=$(netstat -epta 2>/dev/null | grep $PID 2>/dev/null | grep amqp) || test -z "$PID"
then
    echo "nova-scheduler is not connected to AMQP."
    exit $STATE_CRITICAL
fi
 
echo "nova-scheduler is working."
exit $STATE_OK
