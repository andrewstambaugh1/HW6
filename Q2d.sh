Q2d.sh
i=1
while [i<1440]
    do
        python3 Q2c.py NWS > Q2dNWS.txt
        python3 Q2c.py NWSSPC > Q2dNWSSPC.txt
        python3 Q2c.py NWSWPC > Q2dNWSWPC.txt
    i=i+1
    sleep(60)
    done