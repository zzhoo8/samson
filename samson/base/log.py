# coding:utf-8

from functools import wraps


def log(func):
    """
    :param func:
    :return:
    """
    @wraps(func)
    def function_log(*args, **kwargs):
        """
        :return:
        """
        result = func(*args, **kwargs)

        # 要求这里返回的都是dict
        from samson import logger
        try:
            logger.info(args.__str__() + func.__name__ + " " + kwargs.__str__() + "\n" + result.__str__())
        except Exception, e:
            logger.error(e.message)

        return result

    return function_log
