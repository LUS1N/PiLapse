import argparse

from google_api.uploaders.drive import Drive
from google_api.uploaders.youtube import Youtube


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('app_name', help='Name of the application.')
    parser.add_argument('file_path', help='Path to file to upload.')
    parser.add_argument('name', help='File name to upload.')
    parser.add_argument('video_description',
                        help='Description for video on youtube')
    parser.add_argument('--tags', nargs='*')
    return parser.parse_args()


def drive_upload(arguments):
    print('Initiating uploading to drive')
    app_name = arguments.app_name
    drive = Drive(app_name)

    try:
        print('Looking for root folder for application: %s' % app_name)
        project_root_folder = drive.find_folder(app_name)
    except:
        print('Root dir for application not found, creating it..')
        project_root_folder = drive.create_folder_in_root(app_name)

    print('Creating a folder (%s) for the video' % arguments.name)
    folder = drive.create_folder(project_root_folder['id'], arguments.name)

    print('Uploading file to "%s/%s"' % (app_name, arguments.name))
    file = drive.upload_file(folder['id'], arguments.name, arguments.file_path)

    if file:
        print("File %s succesfully uploaded." % arguments.name)
        print(file)
    else:
        print('Error uploading file to drive')


def youtube_upload(arguments):
    app_name = arguments.app_name
    print('Building youtube client')
    youtube = Youtube(app_name)

    print('Uploading video "%s" to youtube' % arguments.name)
    
    response = youtube.upload_video(arguments.file_path,
                            arguments.name,
                            arguments.video_description,
                            arguments.tags,
                            None,
                            'public')
    print(response)


if __name__ == '__main__':
    arguments = parse_args()
    print(arguments)
    drive_upload(arguments)
    youtube_upload(arguments)

    
