from css_formatting import *
import os

def create_custom_input_button(st):
    '''This Method adds CSS properties to Streamlit's st.text_input() button 
        to make it look eleganct
    '''
    st.markdown(custom_input_bar,unsafe_allow_html=True)
    st.markdown(custome_input_bar_top,unsafe_allow_html=True)

def check_input_url(playlisturl, YouTube, Playlist, st):
    '''This method checks whether the entered URL is correct or not. URL entered will
       be passed into pytube's YouTube() method incase of single Youtube video or Playlist() 
       method in case of a Youtube Playlist 
    '''
    src = None
    playlist = list()
    if "playlist" in playlisturl.lower():
        try:
            playlist = Playlist(playlisturl)
            src = f"https://www.youtube.com/embed/videoseries?{playlisturl.split('?')[-1]}"
        except:
            st.image('oops3.jpg')
            # st.error("The URL you have entered does not exist. Please check & enter correct URL")
            st.stop()
    else:
        try:
            yt = YouTube(playlisturl)
            src = f"https://www.youtube.com/embed/{playlisturl.split('/')[-1]}"
            playlist.append(playlisturl)
        except:
            st.image('oops3.jpg')
            # st.error("The URL you have entered does not exist. Please check & enter correct URL")
            st.stop()
    return playlist, src

def create_zip_folder_mp4(py7zr):
    ''' this method creates a 7zip file for storing converted mp4 audios from a
        Youtube Playlist'''
    try:
        with py7zr.SevenZipFile('YT_Playlist_mp4.7z', 'w') as archive:
            archive.writeall('target/')
    except:
        pass

def create_zip_folder_mp3(py7zr):
    ''' this method creates a 7zip file for storing converted mp3 audios from a
        Youtube Playlist'''

    try:
        with py7zr.SevenZipFile('YT_Playlist_mp3.7z', 'w') as archive:
            archive.writeall('target/')
    except:
        pass

def updating_progress_bar_while_downloading_audios(st, playlist, YouTube,py7zr, mp, time):
    '''This method will setup a progress bar showing the progress while video/Playlist
       from Youtube is being converted into .mp4 and .mp3 audio formats
    '''
    
    filename = ""
    time.sleep(1)
    latest_iteration = st.sidebar.empty()
    bar = st.sidebar.progress(0)
    unit_percentage_progress = 100/len(playlist)
    
    if len(playlist) ==1:
        try:
            tmp = YouTube(playlist[0]).streams.filter(only_audio=True).first().download().split("\\")[-1]
            filename = tmp[:-4]
            st.sidebar.info("Conversion is in progress\nKeep checking below for updates on progress")
            new_file = mp.AudioFileClip(tmp)
            new_file.write_audiofile(tmp[0:-4]+".mp3")
            st.sidebar.info(f"Converted - {filename}")
            latest_iteration.text(f'100% 1 of 1')
            bar.progress(100)
        except Exception as e:
            st.exception(e)
            if "unavailable" in str(e).lower():
                st.sidebar.error("Sorry😔. This video is unavailable to download")
            st.stop()
    else:
        for i in range(0,100):
            try:
                tmp = YouTube(playlist[i]).streams.filter(only_audio=True).first().download().split("\\")[-1]
            except Exception as e:
                st.exception(e)
                st.stop()

            with py7zr.SevenZipFile('YT_Playlist_mp4.7z', 'a') as archive:
                archive.write(tmp)
            
            new_file = mp.AudioFileClip(tmp)
            mp3_file = new_file.write_audiofile(tmp[0:-4]+".mp3")
        
            with py7zr.SevenZipFile('YT_Playlist_mp3.7z', 'a') as archive:
                #st.write("inside")
                file_name = tmp[0:-4]+".mp3"
                archive.write(file_name)
                #st.write("done arc")

            current_progress = (i+1)*unit_percentage_progress
            latest_iteration.text(f'{round(current_progress)}% {i+1} of {len(playlist)}')
            st.sidebar.info(f"Converted - {tmp[0:-4]}")

            if current_progress+unit_percentage_progress > 100:
                current_progress = 100
                latest_iteration.text(f'100% {len(playlist)} of {len(playlist)}')
                bar.progress(round(current_progress))
                break
            else:
                bar.progress(round(current_progress))
    return filename
    
def download_mp3_audio(st, py7zr,filename=None):
    '''this method reads the converted mp3 playlist(zip file) / or single mp3 audio file
       calculate the size for that file and create a download button for user to download
       the file
    '''

    size, target_size = None, ""
    if filename != None:
        size = round(os.path.getsize(filename)/1024, 2)
        target_size = f"{size}KB"
        if size // 1024 != 0:
            size = round(size/1024, 2)
            target_size = f"{size}MB"
        if size // 1024 != 0:
            size = round(size/1024, 2)
            target_size = f"{size}GB"
        #st.write("inside open method")
       
        with open(filename,"rb") as f:
                btn = st.download_button(
                    label=f"🎸 MP3 {target_size}",
                    data=f,
                    file_name=filename[26:],
                    mime="application/octet-stream"
                )
    else:
        with open("YT_Playlist_mp3.7z", "rb") as download_playlist:
            with py7zr.SevenZipFile('YT_Playlist_mp3.7z', 'r') as zip:
                size = round(int(zip.archiveinfo().size)/1024, 2)
                target_size = f"{size}KB"
                if size // 1024 != 0:
                    size = round(size/1024, 2)
                    target_size = f"{size}MB"
                if size // 1024 != 0:
                    size = round(size/1024, 2)
                    target_size = f"{size}GB"

            with open("YT_Playlist_mp3.7z", "rb") as download_playlist:
                btn = st.download_button(
                    label=f"📁 MP3 {target_size}",
                    data=download_playlist,
                    file_name="YT_Playlist_mp3.7z",
                    mime="application/x-7z-compressed"
                )
                st.markdown(download_button_css_main, unsafe_allow_html=True) 

def download_mp4_audio(st, py7zr, filename=None):
    '''this method reads the converted mp3 playlist(zip file) / or single mp3 audio file
       calculate the size for that file and create a download button for user to download
       the file
    '''
    size, target_size = None, ""
    if filename != None:
        size = round(os.path.getsize(filename)/1024, 2)
        target_size = f"{size}KB"
        if size // 1024 != 0:
            size = round(size/1024, 2)
            target_size = f"{size}MB"
        if size // 1024 != 0:
            size = round(size/1024, 2)
            target_size = f"{size}GB"
        #st.write("inside open method")
       
        with open(filename,"rb") as f:
                btn = st.download_button(
                    label=f"🎸MP4 {target_size}",
                    data=f,
                    file_name=filename[26:],
                    mime="application/octet-stream"
                )
    else:
        with open("YT_Playlist_mp4.7z", "rb") as download_playlist:
            with py7zr.SevenZipFile('YT_Playlist_mp4.7z', 'r') as zip:
                size = round(int(zip.archiveinfo().size)/1024, 2)
                target_size = f"{size}KB"
                if size // 1024 != 0:
                    size = round(size/1024, 2)
                    target_size = f"{size}MB"
                if size // 1024 != 0:
                    size = round(size/1024, 2)
                    target_size = f"{size}GB"

            with open("YT_Playlist_mp4.7z", "rb") as download_playlist:
                btn = st.download_button(
                    label=f"📁 MP4 {target_size}",
                    data=download_playlist,
                    file_name="YT_Playlist_mp4.7z",
                    mime="application/x-7z-compressed"
                )
                st.markdown(download_button_css_main, unsafe_allow_html=True)
