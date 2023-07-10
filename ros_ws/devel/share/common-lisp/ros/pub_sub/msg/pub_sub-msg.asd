
(cl:in-package :asdf)

(defsystem "pub_sub-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TestMessage" :depends-on ("_package_TestMessage"))
    (:file "_package_TestMessage" :depends-on ("_package"))
  ))