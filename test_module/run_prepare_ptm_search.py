import argparse
from test_module.config import Config
from test_module.preprocessing.prepare_ptm_search import prepare_ptm_search

def main():
    parser = argparse.ArgumentParser(description="Prepare PTM database and configs")
    parser.add_argument('--config', type=str, default='pipeline.cfg', help='Path to config file')
    args = parser.parse_args()

    config = Config(args.config)
    print('Run prepare ptm search !')
    # print(config.experiment_name)
    # print(config.analysis_index)
    # print(config.search_mode)
    # print(config.fdr_strategy)
    # print(config.fasta_path)
    # print(config.work_dir)
    # print(config.base_config_path)
    prepare_ptm_search(config)
