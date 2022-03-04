import cv2
import streamlit as st
import numpy as np
from PIL import Image

st.subheader('Pencil sketch your image using python opencv')

st.image("upload.jpg", width=400)
uploaded_file = st.file_uploader("Upload Image")

#Function call
if uploaded_file:

    image = Image.open(uploaded_file)
    # st.image(image, caption='Input', use_column_width=True)
    img_array = np.array(image)
    cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
    #Read Image
    img = cv2.imread("out.jpg")

    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img = cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img = cv2.GaussianBlur(invert_img, (7, 7), 0)

    # Invert Blurred Image
    invblur_img = cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)
    st.image(sketch_img)

    # Save Sketch
    cv2.imwrite('sketch.png', sketch_img)

    # # Display sketch
    # cv2.imshow('sketch image', sketch_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    with open("sketch.png", "rb") as file:
     btn = st.download_button(
         label="Download image",
         data=file,
         file_name="sketch.png",
         mime="image/png"
     )
