import argparse

def parse_arg():
    parser = argparse.ArgumentParser(description='generate cuda/cudnn set up script.')
    parser.add_argument('--cuda', default='9.0')
    parser.add_argument('--cudnn', default='7.4')
    return parser.parse_args()

VALID_PAIR=(('7.0', '9.0'),
            ('7.2', '9.0'),
            ('7.4', '9.0'),
            ('7.2', '9.2'),
            ('7.4', '9.2'),
            ('7.4', '10.0'),
            ('7.5', '9.0'),
            ('7.5', '9.2'),
            ('7.5', '10.0'))

cudnn = ['7.0.5.15-1+cuda9.0',
'7.2.1.38-1+cuda9.0',
'7.4.2.24-1+cuda9.0',
'7.2.1.38-1+cuda9.2',
'7.4.2.24-1+cuda9.2',
'7.4.2.24-1+cuda10.0',
'7.5.0.56-1+cuda9.0',
'7.5.0.56-1+cuda9.2',
'7.5.0.56-1+cuda10.0']
def cuda_script_setup(cuda_version):
    version_dict = {
        '9.0': 'cuda-repo-ubuntu1604_9.0.176-1_amd64.deb',
        '9.2': 'cuda-repo-ubuntu1604_9.2.148-1_amd64.deb',
        '10.0': 'cuda-repo-ubuntu1604_10.1.105-1_amd64.deb'
    }
    with open('templates/cuda_script_template.sh') as fp:
        cuda_script = fp.read()
    cuda_script = cuda_script.replace('***cuda-repo***', version_dict[cuda_version])
    cuda_script = cuda_script.replace('***cuda-version***', cuda_version.replace('.', '-'))
    with open('gpu-setup-part1-cuda.sh', 'w') as fp:
        fp.write(cuda_script)


def cudnn_script_setup(cudnn_version,cuda_version):
    cudnn_dict = dict(zip(VALID_PAIR, cudnn))
    with open('templates/cudnn_script_template.sh') as fp:
        data = fp.read()
    data = data.replace('***cudnn-cuda***', cudnn_dict[(cudnn_version,
                                                        cuda_version)])
    with open('gpu-setup-part2-cudnn.sh', 'w') as fp:
        fp.write(data)


def main():
    args = parse_arg()
    cudnn_version = args.cudnn
    cuda_version = args.cuda
    if cuda_version == '10':
        cuda_version = '10.0'
    if cuda_version == '9':
        cuda_version = '9.0'
    if cudnn_version =='7':
        cudnn_version ='7.0'
    input_pair = (cudnn_version, cuda_version)
    assert input_pair in VALID_PAIR, 'We currently only support the following cudnn-cuda pair:\n{}.'.format(VALID_PAIR)
    cuda_script_setup(cuda_version)
    cudnn_script_setup(cudnn_version, cuda_version)


if __name__=='__main__':
    main()
