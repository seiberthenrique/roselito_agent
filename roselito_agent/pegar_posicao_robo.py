import rclpy
from geometry_msgs.msg import PoseStamped

def pegar_posicao_robo(node, buffer, global_frame, robot_frame):
    r'''Captura a pose atual do robô usando o buffer de TF passado por argumento.'''
    try:
        transform = buffer.lookup_transform(
            global_frame,
            robot_frame,
            rclpy.time.Time()
        )
        
        pose = PoseStamped()
        pose.header.frame_id = global_frame
        pose.header.stamp = node.get_clock().now().to_msg()
        
        pose.pose.position.x = transform.transform.translation.x
        pose.pose.position.y = transform.transform.translation.y
        pose.pose.position.z = transform.transform.translation.z
        pose.pose.orientation = transform.transform.rotation
        
        return pose
    except Exception as e:
        node.get_logger().warn(f'Falha ao obter pose: {e}')
        return None