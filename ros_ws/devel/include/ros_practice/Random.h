// Generated by gencpp from file ros_practice/Random.msg
// DO NOT EDIT!


#ifndef ROS_PRACTICE_MESSAGE_RANDOM_H
#define ROS_PRACTICE_MESSAGE_RANDOM_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ros_practice
{
template <class ContainerAllocator>
struct Random_
{
  typedef Random_<ContainerAllocator> Type;

  Random_()
    : random_value(0.0)
    , activity()  {
    }
  Random_(const ContainerAllocator& _alloc)
    : random_value(0.0)
    , activity(_alloc)  {
  (void)_alloc;
    }



   typedef float _random_value_type;
  _random_value_type random_value;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _activity_type;
  _activity_type activity;





  typedef boost::shared_ptr< ::ros_practice::Random_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_practice::Random_<ContainerAllocator> const> ConstPtr;

}; // struct Random_

typedef ::ros_practice::Random_<std::allocator<void> > Random;

typedef boost::shared_ptr< ::ros_practice::Random > RandomPtr;
typedef boost::shared_ptr< ::ros_practice::Random const> RandomConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_practice::Random_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_practice::Random_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ros_practice::Random_<ContainerAllocator1> & lhs, const ::ros_practice::Random_<ContainerAllocator2> & rhs)
{
  return lhs.random_value == rhs.random_value &&
    lhs.activity == rhs.activity;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ros_practice::Random_<ContainerAllocator1> & lhs, const ::ros_practice::Random_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ros_practice

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ros_practice::Random_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_practice::Random_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_practice::Random_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_practice::Random_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_practice::Random_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_practice::Random_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_practice::Random_<ContainerAllocator> >
{
  static const char* value()
  {
    return "06e14fd41d63e9eb5e32e490cf8ee14a";
  }

  static const char* value(const ::ros_practice::Random_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x06e14fd41d63e9ebULL;
  static const uint64_t static_value2 = 0x5e32e490cf8ee14aULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_practice::Random_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_practice/Random";
  }

  static const char* value(const ::ros_practice::Random_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_practice::Random_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 random_value\n"
"string activity\n"
;
  }

  static const char* value(const ::ros_practice::Random_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_practice::Random_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.random_value);
      stream.next(m.activity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Random_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_practice::Random_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_practice::Random_<ContainerAllocator>& v)
  {
    s << indent << "random_value: ";
    Printer<float>::stream(s, indent + "  ", v.random_value);
    s << indent << "activity: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.activity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_PRACTICE_MESSAGE_RANDOM_H
