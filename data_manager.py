"""
Data Manager Module
Handles all data operations including Excel loading, searching, and exporting
Optimized for 5,000-20,000 records with O(1) lookup performance
"""

import pandas as pd
from typing import Dict, Optional, Tuple, List


class DataManager:
    """
    Manages voter data with efficient lookup and attendance tracking
    """
    
    def __init__(self):
        self.df: Optional[pd.DataFrame] = None
        self.voter_card_index: Dict[str, int] = {}  # O(1) lookup by voter card number
        self.required_columns = ["Họ và tên", "Số thẻ cử tri", "Số CCCD"]
        
    def load_excel(self, file_path: str) -> Tuple[bool, str]:
        """
        Load Excel file and prepare data
        
        Args:
            file_path: Path to Excel file
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            # Load Excel file
            df = pd.read_excel(file_path, engine='openpyxl')
            
            # Validate required columns exist
            missing_cols = [col for col in self.required_columns if col not in df.columns]
            if missing_cols:
                return False, f"Missing required columns: {', '.join(missing_cols)}"
            
            # Extract only required columns
            df = df[self.required_columns].copy()
            
            # Data cleaning and normalization
            for col in self.required_columns:
                # Convert to string and trim whitespace
                df[col] = df[col].astype(str).str.strip()
                # Replace NaN or 'nan' string with empty string
                df[col] = df[col].replace(['nan', 'None', 'NaN'], '')
            
            # Add attendance status column
            df['Trạng thái'] = 'Chưa điểm danh'
            
            # Store dataframe
            self.df = df
            
            # Build O(1) lookup index by voter card number
            self._build_index()
            
            return True, f"Successfully loaded {len(df)} voter records"
            
        except FileNotFoundError:
            return False, "File not found"
        except Exception as e:
            return False, f"Error loading file: {str(e)}"
    
    def _build_index(self):
        """Build hash map index for O(1) voter card lookup"""
        self.voter_card_index.clear()
        if self.df is not None:
            # Reset index to ensure continuous 0-based indexing
            self.df.reset_index(drop=True, inplace=True)
            for idx, row in self.df.iterrows():
                voter_card = str(row['Số thẻ cử tri']).strip()
                if voter_card:
                    self.voter_card_index[voter_card] = idx
    
    def mark_attendance(self, voter_card_number: str) -> Tuple[str, Optional[str]]:
        """
        Mark voter as attended by voter card number
        
        Args:
            voter_card_number: Voter card number to search
            
        Returns:
            Tuple of (status: str, full_name: Optional[str])
            Status can be: 'SUCCESS', 'ALREADY_ATTENDED', 'NOT_FOUND'
        """
        if self.df is None:
            return 'NOT_FOUND', None
        
        voter_card_number = voter_card_number.strip()
        
        # O(1) lookup using hash map
        if voter_card_number not in self.voter_card_index:
            return 'NOT_FOUND', None
        
        idx = self.voter_card_index[voter_card_number]
        
        # Check if already attended
        if self.df.at[idx, 'Trạng thái'] == 'Đã điểm danh':
            full_name = self.df.at[idx, 'Họ và tên']
            return 'ALREADY_ATTENDED', full_name
        
        # Mark as attended
        self.df.at[idx, 'Trạng thái'] = 'Đã điểm danh'
        full_name = self.df.at[idx, 'Họ và tên']
        
        return 'SUCCESS', full_name
    
    def verify_voter(self, voter_card_number: str, national_id: str) -> Tuple[str, Optional[str]]:
        """
        Verify voter by both voter card number and national ID
        
        Args:
            voter_card_number: Voter card number
            national_id: National ID (CCCD)
            
        Returns:
            Tuple of (status: str, message: Optional[str])
            Status: 'MATCH', 'ID_MISMATCH', 'NOT_FOUND'
        """
        if self.df is None:
            return 'NOT_FOUND', None
        
        voter_card_number = voter_card_number.strip()
        national_id = national_id.strip()
        
        # Check if voter card exists
        if voter_card_number not in self.voter_card_index:
            return 'NOT_FOUND', None
        
        idx = self.voter_card_index[voter_card_number]
        stored_national_id = str(self.df.at[idx, 'Số CCCD']).strip()
        
        # Verify national ID matches
        if stored_national_id == national_id:
            full_name = self.df.at[idx, 'Họ và tên']
            return 'MATCH', full_name
        else:
            return 'ID_MISMATCH', None
    
    def get_all_records(self) -> List[Tuple]:
        """
        Get all records for display in table
        
        Returns:
            List of tuples (full_name, voter_card, national_id, status)
        """
        if self.df is None:
            return []
        
        records = []
        for _, row in self.df.iterrows():
            records.append((
                row['Họ và tên'],
                row['Số thẻ cử tri'],
                row['Số CCCD'],
                row['Trạng thái']
            ))
        return records
    
    def get_statistics(self) -> Dict[str, int]:
        """
        Get attendance statistics
        
        Returns:
            Dictionary with total, attended, and not_attended counts
        """
        if self.df is None:
            return {'total': 0, 'attended': 0, 'not_attended': 0}
        
        total = len(self.df)
        attended = len(self.df[self.df['Trạng thái'] == 'Đã điểm danh'])
        not_attended = total - attended
        
        return {
            'total': total,
            'attended': attended,
            'not_attended': not_attended
        }
    
    def find_record_index(self, voter_card_number: str) -> Optional[int]:
        """
        Find the dataframe index for a voter card number
        
        Args:
            voter_card_number: Voter card number to search
            
        Returns:
            Index in dataframe or None if not found
        """
        voter_card_number = voter_card_number.strip()
        return self.voter_card_index.get(voter_card_number)
    
    def export_to_excel(self, file_path: str) -> Tuple[bool, str]:
        """
        Export current data to Excel file
        
        Args:
            file_path: Path where to save the Excel file
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if self.df is None:
            return False, "No data to export"
        
        try:
            # Export with all columns including attendance status
            self.df.to_excel(file_path, index=False, engine='openpyxl')
            return True, f"Data exported successfully to {file_path}"
        except Exception as e:
            return False, f"Error exporting file: {str(e)}"
    
    def is_loaded(self) -> bool:
        """Check if data is loaded"""
        return self.df is not None and not self.df.empty
