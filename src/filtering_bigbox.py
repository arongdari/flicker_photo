#!/usr/bin/env python3
import sys
from datetime import datetime

def filtering(lng_min, lat_min, lng_max, lat_max, time_min, time_max, fin, fout):
    """Filtering out all records outside the bounding box: 
       [(lng_min, lat_min), (lng_max, lat_max)]
    """
    assert(lng_min < lng_max)
    assert(lat_min < lat_max)
    assert(isinstance(time_min, datetime))
    assert(isinstance(time_max, datetime))
    assert(time_min < time_max)
    
    # 1    * Photo/video identifier 
    # 2    * User NSID
    # 4    * Date taken
    # 11   * Longitude
    # 12   * Latitude
    # 13   * Accuracy
    # 14   * Photo/video page URL
    # 23   * Photos/video marker (0 = photo, 1 = video)

    with open(fout, 'w') as fo:
        #fo.write('Photo_ID, User_ID, Timestamp, Longitude, Latitude, Accuracy, URL, Marker(photo=0 video=1)\n')
        with open(fin, 'r') as fi:
            for line in fi:
                t = line.strip().split('\t')
                pid    = t[0].strip()
                uid    = t[1].strip()
                time   = t[3].strip()
                lng    = t[10].strip()
                lat    = t[11].strip()
                acc    = t[12].strip()
                url    = t[13].strip()
                marker = t[22].strip()
                
                if len(pid) == 0 or len(uid) == 0 or \
                   len(time) == 0 or len(lng) == 0 or \
                   len(lat) == 0 or len(acc) == 0 or \
                   len(url) == 0 or len(marker) == 0: continue

                lng = float(lng)
                lat = float(lat)
                if lng < lng_min or lng > lng_max: continue
                if lat < lat_min or lat > lat_max: continue

                dt = datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
                if dt < time_min or dt > time_max: continue

                fo.write(pid + ',' + uid + ',' + time + ',' + \
                         str(lng) + ',' + str(lat) + ',' + \
                         acc + ',' + url + ',' + marker + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], 'YFCC100M_DATA_FILE')
        sys.exit(0)

    fin = sys.argv[1]
    fout = './out.' + fin.split('/')[-1]
    lng_min = 141.9
    lat_min = -39.3 
    lng_max = 147.1
    lat_max = -35.8 
    time_min = datetime.strptime('2000-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    time_max = datetime.strptime('2015-03-05 23:59:59', '%Y-%m-%d %H:%M:%S')
    
    filtering(lng_min, lat_min, lng_max, lat_max, time_min, time_max, fin, fout)

