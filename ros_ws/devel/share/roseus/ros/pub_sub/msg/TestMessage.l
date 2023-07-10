;; Auto-generated. Do not edit!


(when (boundp 'ros_practice::TestMessage)
  (if (not (find-package "ros_practice"))
    (make-package "ros_practice"))
  (shadow 'TestMessage (find-package "ros_practice")))
(unless (find-package "ros_practice::TESTMESSAGE")
  (make-package "ros_practice::TESTMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude TestMessage.msg.html


(defclass ros_practice::TestMessage
  :super ros::object
  :slots (_random_value _activity ))

(defmethod ros_practice::TestMessage
  (:init
   (&key
    ((:random_value __random_value) 0.0)
    ((:activity __activity) "")
    )
   (send-super :init)
   (setq _random_value (float __random_value))
   (setq _activity (string __activity))
   self)
  (:random_value
   (&optional __random_value)
   (if __random_value (setq _random_value __random_value)) _random_value)
  (:activity
   (&optional __activity)
   (if __activity (setq _activity __activity)) _activity)
  (:serialization-length
   ()
   (+
    ;; float32 _random_value
    4
    ;; string _activity
    4 (length _activity)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _random_value
       (sys::poke _random_value (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _activity
       (write-long (length _activity) s) (princ _activity s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _random_value
     (setq _random_value (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _activity
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _activity (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get ros_practice::TestMessage :md5sum-) "06e14fd41d63e9eb5e32e490cf8ee14a")
(setf (get ros_practice::TestMessage :datatype-) "ros_practice/TestMessage")
(setf (get ros_practice::TestMessage :definition-)
      "float32 random_value
string activity
")



(provide :ros_practice/TestMessage "06e14fd41d63e9eb5e32e490cf8ee14a")


