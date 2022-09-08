import streamlit as st
from streamlit.components.v1 import iframe
from pytube import YouTube,Playlist
import os
import moviepy.editor as mp
import sys
import py7zr

st.set_page_config(layout="centered", page_icon="\U0001F3AC", page_title="YT Video2Audio Converter")
st.title("Download Playlist from You Tube in .mp4/.mp3 format")

st.write("!!!This app lets you download a public You Tube Playlist!!!")

playlisturl = st.text_input("Enter Playlist URL here", key="playlisturl")
if playlisturl != "":
    playlist = list()
    if "playlist" in playlisturl.lower():
        playlist = Playlist(playlisturl)
        #st.write("try executed successfully")
    else:
        playlist.append(playlisturl)
    #st.write(playlist)


    # Testing download with one song
    #YouTube(playlist[0]).streams.filter(only_audio=True).first().download()



    # download all videos from YT playlist in mp4 audio format.
    # Note : - it will not download video, it will download audio only in mp4 format.
    try:
        # root_path = os.getcwd()
        # temp_path = root_path + "\\Temp_downloaded_songs"
        #st.write(root_path)
        # os.chdir(temp_path)
        'We are processing your Playlist make sure you have a good internet connection for speedy downloads...'

        # Add a placeholder
        try:
            with py7zr.SevenZipFile('YT_Playlist.7z', 'w') as archive:
                archive.writeall('target/')
        except:
            pass
        # with py7zr.SevenZipFile('YT_Playlist.7z', 'a') as archive:
        #     archive.write("requirements.txt")
        latest_iteration = st.empty()
        bar = st.progress(0)

        unit_percentage_progress = 100//len(playlist)

        for i in range(0,100):
            # tmp = YouTube(playlist[i]).streams.filter(only_audio=True).first().download()
            
            with py7zr.SevenZipFile('YT_Playlist.7z', 'a') as archive:
                st.write("inside zip")
                #archive.write("requirements.txt")
                #st.write(playlist.videos[i].title)
                #st.write(tmp)
                # tmp = tmp.split("\\")
                # tmp = tmp[-1]
                # st.write(tmp)
                archive.write(YouTube(playlist[i]).streams.filter(only_audio=True).first().download().split("\\")[-1])

            # Update the progress bar with each iteration.
            current_progress = (i+1)*unit_percentage_progress
            latest_iteration.text(f'{current_progress} %')
            #time.sleep(0.1)
            if current_progress+unit_percentage_progress > 100:
                current_progress = 100
                latest_iteration.text(f'{current_progress} %')
                bar.progress(current_progress)
                break
            else:
                bar.progress(current_progress)
        '...and now we\'re done!'
        # time.sleep(0.2)
        # st.balloons()
        # Zip_file_dir = root_path + "\\downloads"
        # os.chdir(Zip_file_dir)
        

        with open("YT_Playlist.7z", "rb") as download_playlist:

            # download_url = create_download_link(download_playlist, 'YT_Playlist.7z')
            # st.markdown(download_url, unsafe_allow_html=True)
            
            btn = st.download_button(
                label="⬇️ Download YourPlaylist",
                data=download_playlist,
                file_name="YT_Playlist.7z",
                mime="application/x-7z-compressed"
            ) 
    except:
        st.write("Something wrong with specified\
        directory. Exception- ", sys.exc_info())
    finally:
        pass
        # os.chdir(root_path)
        # Temp_file_pointer = os.listdir(temp_path)
        # for item in Temp_file_pointer:
        #     if item.endswith(".mp4") or item.endswith(".mp3"):
        #         os.remove(os.path.join(temp_path, item))

        # Zip_file_pointer = os.listdir(Zip_file_dir)
        # for item in Zip_file_pointer:
        #     os.remove(os.path.join(Zip_file_dir, item))
        
        #playlisturl = st.text_input("Enter Playlist URL here",value=,key="playlisturl")
        #st.write(playlisturl)
        #st.write("executing finally. Folders are empty now")


    # # Converting these downloaded mp4 audio to mp3 using moviepy.editor's AudioFile and 
    # # .writeaudiofile function

    # folder = "C:\\Users\\shabisht\\Desktop\\YT_Songs\\"
    # destination = "C:\\Users\\shabisht\\Desktop\\YT_Songs\\mp3\\"
    # for file in os.listdir(folder):
    # if re.search('mp4', file):
    #     mp4_path = os.path.join(folder,file)
    #     mp3_path = os.path.join(destination+file[0:-4]+".mp3")
    #     new_file = mp.AudioFileClip(mp4_path)
    #     new_file.write_audiofile(mp3_path)
