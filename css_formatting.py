# sidebar_css = '''<style>
#                     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
#                         width: 400px;
#                     }
#                     [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
#                         width: 400px;
#                         margin-left: -400px;
#                         }
#                 </style>'''

custome_input_bar_top = ''' <style>
                    input {
                        border:3px solid #05C3DD;
                        font-size:1.4em;
                        width:100%;
                        padding:.25em .5em .3125em;
                        color:BLACK;
                        border-radius:5em;
                        background:#FFFAFA;
                    }
                </style>
                '''

custom_input_bar = '''<input type="text" 
                        placeholder="Enter Video/Playlist URL..." 
                        id="ip1"/>'''

video_iframe = '''
                    <center>
                      <iframe src="{}"
                      width="100%"
                      height="100%"
                      title="YouTube video player" 
                      frameborder="0"
                      allow="accelerometer; autoplay; 
                    clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
                    </iframe></center>
                '''


download_button_css_main = '''<style>
                    .css-ahw0vf{
                        background: rgb(0, 66, 128);
                        display: inline-flex;
                        border-radius: 5em;
                        color: white;
                        border: 2px solid #FFFFFF;
                        }
                        </style>
                    '''

download_button_css_sidebar = '''<style>
                    .css-13s3n47{
                        background: #05C3DD;
                        display: inline-flex;
                        border-radius: 10rem;
                        margin: 0px;
                        line-height: 2.6;
                        color: white;
                        border: 3px solid #FFFFFF;
                        }
                        </style>
                    '''

st_input_bar_top = ''' <style>
                        .st-br {
                            background-color: #FFFAFA;
                            border-radius: 5em;
                        }
                        .st-bq {
                            border-bottom-color: #05C3DD;
                        }
                        .st-bp {
                            border-top-color: #05C3DD;
                        }
                        .st-bo {
                            border-right-color: #05C3DD;
                        }
                        .st-bn {
                            border-left-color: #05C3DD;
                        }
                        .st-ah {
                            line-height: 1.6em;
                        }
                        .st-af {
                            font-size: 1.1em;
                        }
                        .st-bg {
                            border-bottom-width: 0.3em;
                        }
                        .st-bf {
                            border-top-width: 0.3em;
                        }
                        .st-be {
                            border-right-width: 0.3em;
                        }
                        .st-bd {
                            border-left-width: 0.3em;
                        }
                        .st-cj {
                            border-left-color: #FF4B4B;
                        }
                        .st-cm {
                            border-bottom-color: #FF4B4B;
                        }
                        .st-cl {
                            border-top-color: #FF4B4B;
                        }
                        .st-ck {
                            border-right-color: #FF4B4B;
                        }

                    </style>
                    '''

progress_result_sidebar_div = '''<style>
                                    h1 {
                                            color:Green;
                                        }
                                    div.scroll {
                                        margin:4px, 4px;
                                        padding:4px;
                                        background-color: green;
                                        width: 500px;
                                        height: 110px;
                                        overflow-x: hidden;
                                        overflow-y: auto;
                                        text-align:justify;
                                    }
                                </style>
                                <div class="scroll">
                                
                                </div>
                            '''
