import unittest
from unittest.mock import patch, mock_open

# 测试用的伪数据
IndexSystemPocs = ['poc1', 'poc2']
PocsYamlContent = '''
SiteRequests:
  Implement:
    ImArray:
      - Inter: /usr/bin/python3
        InterArgs:
          - arg1
          - arg2
        Exec: exploit.py
        Args:
          - arg3
          - arg4
    ExpireTime: 10
SiteInfo:
  Solution: "这是一个测试解决方案"
'''


class TestSystemMain(unittest.TestCase):

    @patch('SystemPoc.open', new_callable=mock_open, read_data=PocsYamlContent)
    @patch('os.system')
    @patch('os.remove')
    def test_SystemMain(self, mock_remove, mock_system, mock_file):
        # 假设 IndexSystemPocs[0] 对应的 poc 文件内容为 PocsYamlContent

        # 测试是否正确打开了文件
        mock_file.assert_called_with('./data/SystemPocs/poc1/poc1.yaml', 'r', encoding='utf-8')

        # 测试是否正确执行了系统命令
        expected_command = 'timeout 10 /usr/bin/python3 arg1 arg2 ./data/SystemPocs/poc1/exploit.py arg3 arg4 1> ./data/SystemPocs/poc1/result.txt 2>&1'
        mock_system.assert_called_with(expected_command)

        # 测试是否正确删除了结果文件
        mock_remove.assert_called_with('./data/SystemPocs/poc1/result.txt')


# 运行单元测试
if __name__ == '__main__':
    unittest.main()
