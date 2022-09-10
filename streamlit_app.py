import streamlit as st
import streamlit.components.v1 as components
from pytube import YouTube,Playlist
import os
import moviepy.editor as mp
import sys
import py7zr
from css_formatting import *
from methods import *
import time

st.set_page_config(layout="centered", page_icon="\U0001F3AC",
                    page_title="YT Video2Audio Converter",
                    )

with st.sidebar:
    st.markdown(sidebar_css,unsafe_allow_html=True)
    st.image("logo.jpg")

#st.markdown("<br>", unsafe_allow_html=True)
st.image("logo4.png")
   
#st.title("Download Playlist from You Tube in .mp4/.mp3 format")
#create_custom_input_button(st)
playlisturl = st.text_input("", key="playlisturl", placeholder="Enter Video/Plalist link here...")
st.markdown(st_input_bar_top, unsafe_allow_html=True)
if playlisturl!="":
    playlist, src = check_input_url(playlisturl, YouTube, Playlist, st)
    with st.sidebar:
        st.empty()
        st.markdown(video_iframe.format(src), unsafe_allow_html=True)
    
    try:
        create_zip_folder_mp4(py7zr)
        create_zip_folder_mp3(py7zr)

        updating_progress_bar_while_downloading_audios(st, playlist, YouTube, py7zr, mp)
        st.success("!!!Your Playlist is ready to download!!!")
        time.sleep(1)
        st.balloons()
        with st.sidebar:
            st.markdown("</br>", unsafe_allow_html=True)
            download_mp4_audio(st, py7zr)
            download_mp3_audio(st, py7zr)
    except:
        st.write("Something wrong with specified\
        directory. Exception- ", sys.exc_info())