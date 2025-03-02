import unittest
from unittest.mock import patch, mock_open

# 全局变量，根据实际情况设置
IndexKernelPocs = ['poc1', 'poc2']  # 示例Poc名称列表
Result = []  # 存储结果的列表，需要在测试用例中定义
PocsYaml = {
    'SiteRequests': {
        'Implement': {
            'ImArray': [
                {
                    'Inter': 'python',
                    'InterArgs': ['arg1', 'arg2'],
                    'Exec': 'exploit.py',
                    'Args': ['arg3', 'arg4']
                }
            ],
            'ExpireTime': 10
        }
    },
    'SiteInfo': {
        'Solution': 'Dummy solution'
    }
}


class TestKernelMain(unittest.TestCase):

    @patch('KernelPoc.open', new_callable=mock_open, read_data='some data')
    @patch('KernelPoc.os')
    def test_KernelMain(self, mock_os, mock_file):
        global Result, PocsYaml

        # 模拟IndexKernelPocs[i]中对应的文件内容
        mock_file.return_value.__enter__.return_value.read.return_value = yaml.dump(PocsYaml)

        # 执行待测函数
        IndexKernelPocs(0)  # 假设i=0时对应的poc名称是'poc1'

        # 验证是否正确读取了yaml文件
        mock_file.assert_called_with('./data/KernelPocs/poc1/poc1.yaml', 'r', encoding='utf-8')

        # 验证是否执行了预期的系统命令
        expected_command = ('timeout 10 python arg1 arg2 ./data/KernelPocs/poc1/exploit.py arg3 arg4 ' +
                            '1> ./data/KernelPocs/poc1/result.txt 2>&1')
        mock_os.system.assert_called_with(expected_command)

        # 验证结果是否已正确添加到Result列表中
        self.assertEqual(len(Result), 1)
        self.assertIn('poc1', Result[0])
        self.assertEqual(Result[0]['poc1']['CheckResult'], 0)  # 假设检查结果为0
        self.assertEqual(Result[0]['poc1']['solution'], PocsYaml['SiteInfo']['Solution'])

        # 清理全局变量以避免测试之间的干扰
        Result = []


if __name__ == '__main__':
    unittest.main()
