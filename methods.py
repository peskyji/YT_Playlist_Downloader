from css_formatting import *

def create_custom_input_button(st):
    st.markdown(custom_input_bar,unsafe_allow_html=True)
    st.markdown(custome_input_bar_top,unsafe_allow_html=True)

def check_input_url(playlisturl, YouTube, Playlist, st):
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
    try:
        with py7zr.SevenZipFile('YT_Playlist_mp4.7z', 'w') as archive:
            archive.writeall('target/')
    except:
        pass

def create_zip_folder_mp3(py7zr):
    try:
        with py7zr.SevenZipFile('YT_Playlist_mp3.7z', 'w') as archive:
            archive.writeall('target/')
    except:
        pass

def updating_progress_bar_while_downloading_audios(st, playlist, YouTube,py7zr, mp):
    latest_iteration = st.empty()
    bar = st.progress(0)
    unit_percentage_progress = 100/len(playlist)
    
    for i in range(0,100):
        tmp = YouTube(playlist[i]).streams.filter(only_audio=True).first().download().split("\\")[-1]
        with py7zr.SevenZipFile('YT_Playlist_mp4.7z', 'a') as archive:
            archive.write(tmp)
        try:
            st.write(f"{YouTube(playlist[i]).title} downloaded")
        except:
            st.write(f"{playlist.videos[i]} downloaded")
            # Update the progress bar with each iteration.

        new_file = mp.AudioFileClip(tmp)
        mp3_file = new_file.write_audiofile(tmp[0:-4]+".mp3")
        with py7zr.SevenZipFile('YT_Playlist_mp3.7z', 'a') as archive:
            #st.write("inside")
            file_name = tmp[0:-4]+".mp3"
            archive.write(file_name)
            #st.write("done arc")

        current_progress = (i+1)*unit_percentage_progress
        latest_iteration.text(f'{round(current_progress)}% {i+1} of {len(playlist)}')
        if current_progress+unit_percentage_progress > 100:
            current_progress = 100
            latest_iteration.text(f'100% {len(playlist)} of {len(playlist)}')
            bar.progress(round(current_progress))
            break
        else:
            bar.progress(round(current_progress))
    
def download_mp3_audio(st, py7zr):
    size, target_size = None, ""
    with open("YT_Playlist_mp3.7z", "rb") as download_playlist:
        with py7zr.SevenZipFile('YT_Playlist_mp3.7z', 'r') as zip:
            size = round(int(zip.archiveinfo().size)/1024, 2)
            target_size = f"{round(size)} KB"
            if size // 1024 != 0:
                size = round(size/1024, 2)
                target_size = f"{round(size)} MB"
            if size // 1024 != 0:
                size = round(size/1024, 2)
                target_size = f"{round(size)} GB"

        with open("YT_Playlist_mp3.7z", "rb") as download_playlist:
            btn = st.download_button(
                label=f"⬇️ MP3 {target_size}",
                data=download_playlist,
                file_name="YT_Playlist_mp3.7z",
                mime="application/x-7z-compressed"
            )
            st.markdown(download_button_css_sidebar, unsafe_allow_html=True)

def download_mp4_audio(st, py7zr):
    size, target_size = None, ""
    with open("YT_Playlist_mp4.7z", "rb") as download_playlist:
        with py7zr.SevenZipFile('YT_Playlist_mp4.7z', 'r') as zip:
            size = round(int(zip.archiveinfo().size)/1024, 2)
            target_size = f"{round(size)} KB"
            if size // 1024 != 0:
                size = round(size/1024, 2)
                target_size = f"{round(size)} MB"
            if size // 1024 != 0:
                size = round(size/1024, 2)
                target_size = f"{round(size)} GB"

        with open("YT_Playlist_mp4.7z", "rb") as download_playlist:
            btn = st.download_button(
                label=f"⬇️ MP4 {target_size}",
                data=download_playlist,
                file_name="YT_Playlist_mp4.7z",
                mime="application/x-7z-compressed"
            )
            st.markdown(download_button_css_sidebar, unsafe_allow_html=True)