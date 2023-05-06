import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import cv2
import numpy as np
import time


class MyMediaPlayer():
	def __init__(self):
		self.detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		self.detector_eye = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
		self.cap = cv2.VideoCapture(0)
		self.cap_video = cv2.VideoCapture("nnxc-360.mp4")


	def music_video_book(self, target_dir):

		# Display the name of a book
		if target_dir == "book":
			print("War and Peace")

		# Play a song
		elif target_dir == "music":
			music = vlc.MediaPlayer("07 Harighe Sabz.mp3")

			music.play()

			time.sleep(15)	

		# Play a movie trailer
		elif target_dir == "movie":

			while True:
				ret_video, frame_video = self.cap_video.read()

				if ret_video:
				
					cv2.imshow("Webcam", frame_video)

					q = cv2.waitKey(1)
					if q == ord('q'):
						break
				else:
					break


			self.cap_video.release()
			cv2.destroyAllWindows()


		else:
			print("Please enter one of the following:")
			print("book, music, movie")


	def stream_webcam(self, face_display="yes"):

		while True:
			ret, frame = self.cap.read()

			if ret:
				frame = cv2.flip(frame, 1)
				frame_blur = frame.copy()

				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

				# Find face coordinates
				results = self.detector.detectMultiScale(gray)

				for (x, y, w, h) in results:

					# Identify the face
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
					gray_little = gray[y:y+h, x:x+w]

					# Find the coordinates of the eyes
					results_eye = self.detector_eye.detectMultiScale(gray_little)

					
					for (x1, y1, w1, h1) in results_eye:

						# Identify the eyes
						cv2.rectangle(frame, (x+x1, y+y1), (x+x1+w1, y+y1+h1), (255, 0, 0), 2)

					# blur the face
					frame_blur_little = frame_blur[y:y+h, x:x+w]
					frame_blur_little = cv2.GaussianBlur(frame_blur_little, (105, 105), 0)
					frame_blur[y:y+h, x:x+w] = frame_blur_little
				
				if face_display=="no":
					cv2.imshow("Webcam", frame_blur)

					q = cv2.waitKey(1)
					if q == ord('q'):
						break
				
				else:
					cv2.imshow("Webcam", frame)

					q = cv2.waitKey(1)
					if q == ord('q'):
						break
			else:
				break

		self.cap.release()
		cv2.destroyAllWindows()


mp = MyMediaPlayer()
#mp.stream_webcam("no") # if you want the face to be blur,, enter "no" as input.
mp.music_video_book("music")