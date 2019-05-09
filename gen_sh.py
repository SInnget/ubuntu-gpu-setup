import argparse
from string import Template


def parse_arg():
    parser = argparse.ArgumentParser(
        description='generate cuda/cudnn set up script.')
    parser.add_argument('--cuda',
                        default='9.0',
                        choices=['9', '9.0', '9.2', '10.0', '10', '10.1'])
    parser.add_argument('--cudnn',
                        default='7.4',
                        choices=['7', '7.0', '7.2', '7.4', '7.5'])
    parser.add_argument('--ubuntu', default='1604', choices=['1604', '1804'])
    return parser.parse_args()


VALID_PAIR = (('7.0', '9.0'), ('7.2', '9.0'), ('7.4', '9.0'), ('7.2', '9.2'),
              ('7.4', '9.2'), ('7.4', '10.0'), ('7.4', '10.1'), ('7.5', '9.0'),
              ('7.5', '9.2'), ('7.5', '10.0'), ('7.5', '10.1'))

cudnn = [
    '7.0.5.15-1+cuda9.0', '7.2.1.38-1+cuda9.0', '7.4.2.24-1+cuda9.0',
    '7.2.1.38-1+cuda9.2', '7.4.2.24-1+cuda9.2', '7.4.2.24-1+cuda10.0',
    '7.4.2.24-1+cuda10.1', '7.5.0.56-1+cuda9.0', '7.5.0.56-1+cuda9.2',
    '7.5.0.56-1+cuda10.0', '7.5.0.56-1+cuda10.1'
]


def cuda_script_setup(cuda_version, ubuntu_version='ubuntu1604'):
    version_dict = {
        '9.0': 'cuda-repo-${UBU_V}_9.0.176-1_amd64.deb',
        '9.2': 'cuda-repo-${UBU_V}_9.2.148-1_amd64.deb',
        '10.0': 'cuda-repo-${UBU_V}_10.0.130-1_amd64.deb',
        '10.1': 'cuda-repo-${UBU_V}_10.1.105-1_amd64.deb'
    }
    with open('templates/cuda_script_template.sh') as fp:
        cuda_script = fp.read()
    cuda_repo = Template(
        version_dict[cuda_version]).substitute(UBU_V=ubuntu_version)
    cuda_script = Template(cuda_script).substitute(
        cuda_repo=cuda_repo,
        cuda_version=cuda_version.replace('.', '-'),
        UBU_V=ubuntu_version)
    with open('gpu-setup-part1-cuda.sh', 'w') as fp:
        fp.write(cuda_script)


def cudnn_script_setup(cudnn_version,
                       cuda_version,
                       ubuntu_version='ubuntu1604'):
    cudnn_dict = dict(zip(VALID_PAIR, cudnn))
    with open('templates/cudnn_script_template.sh') as fp:
        data = fp.read()
    data = Template(data).substitute(UBU_V=ubuntu_version,
                                     CUDNN_CUDA=cudnn_dict[(cudnn_version,
                                                            cuda_version)])
    with open('gpu-setup-part2-cudnn.sh', 'w') as fp:
        fp.write(data)


def main():
    args = parse_arg()
    cudnn_version = args.cudnn
    cuda_version = f'{float(args.cuda):.1f}'

    ubuntu_version = 'ubuntu' + args.ubuntu
    input_pair = (cudnn_version, cuda_version)
    assert input_pair in VALID_PAIR, 'We currently only support the following cudnn-cuda pair:\n{}.'.format(
        VALID_PAIR)
    try:
        cuda_script_setup(cuda_version, ubuntu_version)
        cudnn_script_setup(cudnn_version, cuda_version, ubuntu_version)
    except:
        pass

if __name__ == '__main__':
    main()
