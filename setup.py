from setuptools import setup, find_packages

setup(
    name="polifact",                           # 包名
    version="1.0.0",                           # 版本号
    author="Yifan Li",                        # 作者名
    author_email="yifanl23@illinois.edu",     # 作者邮箱
    description="A CLI tool to scrape PolitiFact data",  # 简短描述
    long_description=open("README.md").read(), # 从 README.md 读取详细描述
    long_description_content_type="text/markdown",  # README 文件格式
    url="https://github.com/yourusername/polifact", # 项目主页 
    packages=find_packages(),                  # 自动发现包
    install_requires=[                         # 依赖库
        "requests",
        "beautifulsoup4"
    ],
    entry_points={                             # 定义命令行接口
        "console_scripts": [
            "polifact=polifact.scraper:main",
        ]
    },
    classifiers=[                              # 分类信息
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",                   # Python 版本要求
)
