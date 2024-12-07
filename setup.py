from RagLib import setup, find_packages
setup(
        name = 'InternetSearchRagLib',
        version = '0.0.1',
        packages = find_packages(),
        install_requires = [

        ],
        author = 'ryokugyoku',
        author_email = 'ryoku@blueremarks.com',
        description = '入力したワードをもとに、インターネット上の情報を取得するライブラリ',
        long_description = open('README.md').read(),
        long_description_content_type = 'text/markdown',
        url = '',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6'
)