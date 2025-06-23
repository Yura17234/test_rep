''' Config class '''
from pathlib import Path
import configparser
import os

class Config:
    def __init__(self, config_path='default_ptm.cfg'):
        self._config = configparser.ConfigParser()
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file '{config_path}' not found.")
        self._config.read(config_path)

        # Обработка work_dir с поддержкой ~ и относительных путей
        raw_work_dir = self._config.get('paths', 'work_dir')
        self.work_dir = Path(os.path.expanduser(raw_work_dir)).resolve()
        raw_fasta_path = self._config.get('paths', 'fasta_path')
        self.fasta_path = Path(os.path.expanduser(raw_fasta_path)).resolve()
        raw_base_config_path = self._config.get('paths', 'base_config_path')
        self.base_config_path = Path(os.path.expanduser(raw_base_config_path)).resolve()

        # [experiment]
        self.experiment_name = self._config.get('experiment', 'experiment_name')
        self.analysis_index = self._config.get('experiment', 'analysis_index')
        self.search_mode = self._config.get('experiment', 'search_mode')
        self.fdr_strategy = self._config.get('experiment', 'fdr_strategy')

        # [paths]
        # self.fasta_path = self._config.get('paths', 'fasta_path')
        self.output_dir = self.work_dir / f'{self.experiment_name}_PTM_search'
        # self.working_dir = self._config.get('paths', 'working_dir')
        # self.base_config_path = self._config.get('paths', 'base_config_path')

