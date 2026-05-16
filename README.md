POSTURE GUARD 

Ever caught yourself hunching over your desk with a stiff neck at the
end of the day? That's exactly why I built this.
PostureGuard is a real-time posture monitoring desktop app built for
office environments. It runs quietly in the background, watches your
posture through your webcam, and alerts you before the back pain starts.

 -Built entirely in Python
 
 -Used PyQt5 to build the desktop UI with multiple screens: 
   welcome, live monitor, and weekly report.
   
 -Used OpenCV for webcam access and pose detection.
 
 -Integrated YOLOv8(Ultralytics) for accurate real-time pose,
   estimation using body keypoints like shoulders, hips, and head.
   
 -Added an OpenCV Haar cascade fallback so the app works even
   without YOLO installed
   
 -Stored all session data locally as JSON: no database or cloud.
 
 -Used reportlab for PDF export and openpyxl for Excel export.
 
 -Added winsound for alert sounds on Windows.
 
 -Built a multi-screen PyQt5 app with dark/light theme toggle,
   animated alert banners, and live posture ratio bars.

FEATURES
- Real-time posture detection via webcam.
-  Popup alert with sound after sustained bad posture.
-  Custom alert interval set by the user.
-  Do Not Disturb mode for meetings.
-  Weekly posture performance report.
-  Export report as PDF or Excel.
-  Dark and light mode toggle.
-  Multi-user profiles for office teams.

  
  
