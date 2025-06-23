import argparse
from test_module.config import Config
# from ptm_search.preprocessing.preprocessing_main import preprocessing_main

def main():
    parser = argparse.ArgumentParser(description="Prepare PTM database and configs")
    parser.add_argument('--config', type=str, default='pipeline.cfg', help='Path to config file')
    args = parser.parse_args()

    config = Config(args.config)
    print('Run prepare ptm search')
    print(config.experiment_name)
    print(config.analysis_index)
    print(config.base_path)
    print(config.fasta_path)
    print(config.base_config_path)
    # preprocessing_main(config)
