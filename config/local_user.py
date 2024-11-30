# 使用threading.local()可以创建线程局部变量，每个线程对其的访问都是独立的，从而避免了数据竞争的问题
import threading

# 创建一个TLS对象来存储线程局部的用户信息
# 不需要显示的回收用户信息，因为Python的垃圾回收机制会自动处理这些不再被引用的对象。当线程结束时，该线程的所有TLS数据都会随着线程的终止而变得不可访问，并且如果这些数据没有其他线程或全局引用指向它们，它们最终会被Python的垃圾回收器回收。
tls = threading.local()


def set_user_info(user_info):
    """设置当前线程的用户信息"""
    if not hasattr(tls, 'user_info'):
        tls.user_info = {}
        # 假设user_info是一个包含用户数据的字典，并且我们使用某个键（如user_id）来标识用户
    # 这里为了简化，我们直接假设user_info就是用户ID
    tls.user_info['current_user'] = user_info


def get_user_info():
    """获取当前线程的用户信息"""
    if hasattr(tls, 'user_info') and 'current_user' in tls.user_info:
        return tls.user_info['current_user']
    return None  # 如果没有设置用户信息，则返回None


if __name__ == '__main__':
    set_user_info('5443543cdscsdcsc5435')
    print(get_user_info())