import cv2
import mediapipe as mp


class poseDetector():
    def __init__(self, mode=False, model_complexity=1, upBody=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.model_complexity = model_complexity
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.model_complexity, self.upBody, self.smooth,
                                     self.detectionCon, self.trackCon)

    def preRendering(self, results):
        buff_res = results
        try:
            buff_x = self.results.pose_landmarks.landmark[0].x
            buff_y = self.results.pose_landmarks.landmark[0].y
            buff_z = self.results.pose_landmarks.landmark[0].z
        except:
            buff_x = 0
            buff_y = 0
            buff_z = 0
        try:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                if id == 11 or id == 12:
                    lm.y *=0.9
                elif id == 24 or id == 23:
                    lm.y *=0.87
                elif id > 0 and id < 11:
                    lm.x = buff_x
                    lm.y = buff_y
                    lm.z = buff_z
        except:
            return buff_res
        return results

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        self.afterRenderResults = self.preRendering(self.results.pose_landmarks)

        if self.results.pose_landmarks:
            if draw:
                x1, y1 = self.transformCoord(self.afterRenderResults.landmark[11].x,
                                             self.afterRenderResults.landmark[11].y, img)

                x2, y2 = self.transformCoord(self.afterRenderResults.landmark[12].x,
                                             self.afterRenderResults.landmark[12].y, img)

                x3, y3 = self.transformCoord(self.afterRenderResults.landmark[0].x,
                                             self.afterRenderResults.landmark[0].y, img)

                cv2.line(img, (int((x1+x2)/2), int((y1+y2)/2)), (x3, y3),  (255, 255, 255), 3)
                self.mpDraw.draw_landmarks(img, self.afterRenderResults,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def transformCoord(self, cx, cy, img):
        h, w, c = img.shape
        return int(cx * w), int(cy * h)

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                #print(id, lm)
                cx, cy = self.transformCoord(lm.x,lm.y,img)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)
        return self.lmList