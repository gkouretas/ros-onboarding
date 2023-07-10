
(cl:in-package :asdf)

(defsystem "ros_practice-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Random" :depends-on ("_package_Random"))
    (:file "_package_Random" :depends-on ("_package"))
  ))