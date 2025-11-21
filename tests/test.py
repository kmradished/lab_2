import unittest
import os
import tempfile
import shutil
from io import StringIO
import sys

sys.path.append('src')

class TestProg(unittest.TestCase):
    
    def setUp(self):
        self.papka = tempfile.mkdtemp()
        self.papka2 = os.getcwd()
        os.chdir(self.papka2)

        with open('fl1.txt', 'w', encoding='utf-8') as f:
            f.write('первый файл')
        with open('fl2.txt', 'w') as f:
            f.write('второй файл')
        os.makedirs('fold1', exist_ok=True)
    
    def tearDown(self):
        os.chdir(self.papka2)
        shutil.rmtree(self.papka)
        if os.path.exists('shell.log'):
            os.remove('shell.log')
    
    def test_ls(self):
        try:
            from ls import ls
            
            with StringIO() as i:
                old = sys.stdout
                sys.stdout = i
                
                ls('.') 
                
                sys.stdout = old
                rez = i.getvalue()
            
            self.assertIn('fl1.txt', rez)
            self.assertIn('fl2.txt', rez)
            self.assertIn('fold1', rez)
            
        except Exception as e:
            self.fail(f"Ошибка в ls: {e}")
    
    def test_ls_time(self):
        try:
            from ls import ls
            
            with StringIO() as i:
                old = sys.stdout
                sys.stdout = i
                
                ls('. -l')
                
                sys.stdout = old
                rez = i.getvalue()
            
            self.assertIn('fl1.txt', rez)
            self.assertIn('Итого', rez)
            
        except Exception as e:
            self.fail(f"Ошибка в ls -l: {e}")
    
    def test_cat(self):
        try:
            from cat import cat
            
            with StringIO() as i:
                old = sys.stdout
                sys.stdout = i
                
                cat('fl1.txt')
                
                sys.stdout = old
                rez = i.getvalue()
            
            self.assertIn('первый файл', rez)
            
        except Exception as e:
            self.fail(f"Ошибка в cat: {e}")
    
    def test_lg(self):
        try:
            from lg import lg
        
            if os.path.exists('shell.log'):
                os.remove('shell.log')
            
            lg('test_cm')
            
            self.assertTrue(os.path.exists('shell.log'))
            
            with open('shell.log', 'r', encoding='utf-8') as f:
                content = f.read()
                self.assertIn('test_cm', content)
            
        except Exception as e:
            self.fail(f"Ошибка в lg: {e}")
    
    def test_cd(self):
        try:
            from cd import cd
            st = os.getcwd()
            
            os.makedirs('subfolder', exist_ok=True)

            with StringIO() as i:
                old = sys.stdout
                sys.stdout = i
                
                cd('subfolder')  
                
                sys.stdout = old
            
            new = os.getcwd()
            self.assertIn('subfolder', new)
            
            os.chdir(st)

        except Exception as e:
            self.fail(f"Ошибка в cd: {e}")
    
    def test_cp(self):
        try:
            from cp import cp
            
            with StringIO() as i:
                old = sys.stdout
                sys.stdout = i
                
                cp('', 'fl1.txt', 'fl1_cp.txt')  

                sys.stdout = old
            
            self.assertTrue(os.path.exists('fl1_cp.txt'))
        
        except Exception as e:
            self.fail(f"Ошибка в cp: {e}")
    
    def test_mv(self):
        try:
            from mv import mv
            
            with StringIO() as i:
                old = sys.stdout
                sys.stdout = i
                
                mv('fl2.txt', 'fl2_mv.txt')


                sys.stdout = old
            
            self.assertTrue(os.path.exists('fl2_mv.txt'))
            self.assertFalse(os.path.exists('fl2.txt'))
            
        except Exception as e:
            self.fail(f"Ошибка в mv: {e}")
    
    def test_rm(self):
        try:
            from rm import rm
            
            with StringIO() as i:
                old = sys.stdout
                sys.stdout = i
                
                rm('', 'fl1.txt')  

                sys.stdout = old
            
            self.assertFalse(os.path.exists('fl1.txt'))
            
        except Exception as e:
            self.fail(f"Ошибка в rm: {e}")


class TestBibl(unittest.TestCase):
    
    def test_imp(self):
        ftest = [
            ('ls', 'ls'),
            ('cd', 'cd'),
            ('cat', 'cat'),
            ('cp', 'cp'),
            ('mv', 'mv'),
            ('rm', 'rm'),
            ('lg', 'lg')
        ]
        
        for md_name, funct_name in ftest:
            try:
                md = __import__(md_name)
                funct = getattr(md, funct_name)
                self.assertTrue(callable(funct))
                print(f"{md_name}.{funct_name} - OK")
            except Exception as e:
                self.fail(f"{md_name}.{funct_name}: {e}")


if __name__ == '__main__':    
    unittest.main(verbosity=2)
