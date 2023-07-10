; Auto-generated. Do not edit!


(cl:in-package ros_practice-msg)


;//! \htmlinclude Random.msg.html

(cl:defclass <Random> (roslisp-msg-protocol:ros-message)
  ((random_value
    :reader random_value
    :initarg :random_value
    :type cl:float
    :initform 0.0)
   (activity
    :reader activity
    :initarg :activity
    :type cl:string
    :initform ""))
)

(cl:defclass Random (<Random>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Random>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Random)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_practice-msg:<Random> is deprecated: use ros_practice-msg:Random instead.")))

(cl:ensure-generic-function 'random_value-val :lambda-list '(m))
(cl:defmethod random_value-val ((m <Random>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_practice-msg:random_value-val is deprecated.  Use ros_practice-msg:random_value instead.")
  (random_value m))

(cl:ensure-generic-function 'activity-val :lambda-list '(m))
(cl:defmethod activity-val ((m <Random>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_practice-msg:activity-val is deprecated.  Use ros_practice-msg:activity instead.")
  (activity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Random>) ostream)
  "Serializes a message object of type '<Random>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'random_value))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'activity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'activity))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Random>) istream)
  "Deserializes a message object of type '<Random>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'random_value) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'activity) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'activity) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Random>)))
  "Returns string type for a message object of type '<Random>"
  "ros_practice/Random")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Random)))
  "Returns string type for a message object of type 'Random"
  "ros_practice/Random")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Random>)))
  "Returns md5sum for a message object of type '<Random>"
  "06e14fd41d63e9eb5e32e490cf8ee14a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Random)))
  "Returns md5sum for a message object of type 'Random"
  "06e14fd41d63e9eb5e32e490cf8ee14a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Random>)))
  "Returns full string definition for message of type '<Random>"
  (cl:format cl:nil "float32 random_value~%string activity~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Random)))
  "Returns full string definition for message of type 'Random"
  (cl:format cl:nil "float32 random_value~%string activity~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Random>))
  (cl:+ 0
     4
     4 (cl:length (cl:slot-value msg 'activity))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Random>))
  "Converts a ROS message object to a list"
  (cl:list 'Random
    (cl:cons ':random_value (random_value msg))
    (cl:cons ':activity (activity msg))
))
