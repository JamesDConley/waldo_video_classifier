import cv2
from skimage.transform import resize


def get_frames(path, frames_denominator=2):
    """
    Get frames for the video at the given path
    frames_denominator specifies if frames should be dropped, pass 1 for no dropping, 2 to drop every other, 3 to drop 2/3, etc.
    """
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    frames = []
    count = 0
    while success:
        if (count % frames_denominator) == 0:
            frames.append(image)   
        success,image = vidcap.read()
        count += 1
    return frames

def center_crop(image, center_shape=(448, 448)):
    """Crop the given image to the center section of the given size (rectangular)

    Args:
        image (numpy.ndarray): Numpy array representing image with depth in the third (index [2]) of the array
        center_shape (tuple, optional): Region to crop out of the center of the image. Defaults to (448, 448).

    Returns:
        numpy.ndarray: Numpy array representing the cropped slice of the image
    """
    side_crops = (image.shape[0] - center_shape[0]) // 2
    top_n_bottom_crops = (image.shape[1] - center_shape[1]) // 2
    cropped_image = image[side_crops:-side_crops,top_n_bottom_crops:-top_n_bottom_crops]
    return cropped_image


def process_frame(frame, precrop_shape=(448, 448), input_shape=(224, 224)):
    """Crop a frame down into the precrop shape, then downscape to the given input shape

    Args:
        frame (numpy.ndarray): numpy array representing a frame to process, last index should be depth
        precrop_shape (tuple, optional): The region to crop out of the center of the image before downscaling. Defaults to (448, 448).
        input_shape (tuple, optional): The final size to downscale to. Defaults to (224, 224).

    Returns:
        numpy.ndarray: Numpy array 
    """
    cropped = center_crop(frame, center_shape=precrop_shape) /255
    resized_image = resize(
        cropped,
        input_shape,
        order=3, # Bicubic interpolation
        preserve_range=True,
    )
    return resized_image