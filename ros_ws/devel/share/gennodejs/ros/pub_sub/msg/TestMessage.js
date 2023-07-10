// Auto-generated. Do not edit!

// (in-package ros_practice.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class TestMessage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.random_value = null;
      this.activity = null;
    }
    else {
      if (initObj.hasOwnProperty('random_value')) {
        this.random_value = initObj.random_value
      }
      else {
        this.random_value = 0.0;
      }
      if (initObj.hasOwnProperty('activity')) {
        this.activity = initObj.activity
      }
      else {
        this.activity = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TestMessage
    // Serialize message field [random_value]
    bufferOffset = _serializer.float32(obj.random_value, buffer, bufferOffset);
    // Serialize message field [activity]
    bufferOffset = _serializer.string(obj.activity, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TestMessage
    let len;
    let data = new TestMessage(null);
    // Deserialize message field [random_value]
    data.random_value = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [activity]
    data.activity = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.activity);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ros_practice/TestMessage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '06e14fd41d63e9eb5e32e490cf8ee14a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 random_value
    string activity
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TestMessage(null);
    if (msg.random_value !== undefined) {
      resolved.random_value = msg.random_value;
    }
    else {
      resolved.random_value = 0.0
    }

    if (msg.activity !== undefined) {
      resolved.activity = msg.activity;
    }
    else {
      resolved.activity = ''
    }

    return resolved;
    }
};

module.exports = TestMessage;
