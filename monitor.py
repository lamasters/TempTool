import os, sys, time

stime = time.time()
while True:
    
    if time.time() - stime > 0.5:
        stream = os.popen('/opt/vc/bin/vcgencmd measure_temp')
        output = stream.read()
        temp = float(output.split('=')[1].split('\'')[0])

        percent = int((temp - 10) / 90.0 * 100)

        sys.stdout.write('\r10\'C [' + '|' * percent + ' ' * (90 - percent) + '] 100\'C ' + str(temp) + '\'C')
        sys.stdout.flush()
        stime = time.time()