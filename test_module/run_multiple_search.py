import argparse
from test_module.config import Config
# from ptm_search.search.multiple_search import multiple_search

def main():
    parser = argparse.ArgumentParser(description="Run IdentiPy PTM search")
    parser.add_argument('--config', type=str, default='pipeline.cfg', help='Path to config file')
    args = parser.parse_args()

    config = Config(args.config)
    print('Run multiple search')
    print(config.experiment_name)
    print(config.analysis_index)
    print(config.search_mode)
    print(config.fdr_strategy)
    print(config.fasta_path)
    print(config.work_dir)
    print(config.base_config_path)
    # multiple_search(config)
