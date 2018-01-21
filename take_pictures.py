import argparse
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os


def take_pictures(film_until, dir, picture_number, resolution, interval, annotate=True):
    """ Takes a picture every *interval* seconds.
        Saves it in *dir*, named in a format %06d.png.
        Starting with parameter *picture_number*
        Films until *film_until* hour (integer).
        Resolution is set to *resolution* (tuple of integers).
        Annotates each picture with HH:MM on top of the picture if
        *annotate* == True
    """

    print("Script to take pictures starting.")
    
    if not resolution:
        print('Setting default resolution of 1920x1080')
        resolution = (1920, 1080)
        
    camera = PiCamera()
    camera.resolution = resolution
    camera.start_preview()

    if not picture_number:
        print('Will start counting pictures at 1')
        picture_number = 1


    if not interval:
        print('Setting default picture interval of 4 seconds.')
        interval = 4

    while True:
        time = datetime.now().time()

        if annotate:
            camera.annotate_text = "%02d : %02d" % (time.hour, time.minute)

        camera.capture('%s/%06d.png' % (dir, picture_number))

        print("%d - %02d : %02d : %02d" %
              (picture_number, time.hour, time.minute, time.second))

        picture_number += 1

        if time.hour == film_until:
            break

        sleep(interval)

    camera.stop_preview()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'film_until', help='Stop taking pictures at this hour.', type=int)

    parser.add_argument(
        'dir', help='Put pictures in this directory.', type=str)

    parser.add_argument('-p', '--picture_number',
                        help='Start naming pictures at this number.', type=int)

    parser.add_argument(
        '-i', '--interval', help='Seconds between pictures', type=int)

    parser.add_argument("-a", "--annotate", action="store_true",
                        help="Annotate pictures with time it was taken")

    arguments = parser.parse_args()

    take_pictures(film_until=arguments.film_until,
                  dir=arguments.dir,
                  picture_number=arguments.picture_number,
                  resolution=None,
                  interval=arguments.interval,
                  annotate=arguments.annotate)
