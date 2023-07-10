

from pymarc import MARCReader

with open ('/Users/ep9k/Desktop/metacoll.VA@.new.W20230519.T064052.DegruyterPPplus2021.1.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record.as_json(indent=2))
        
        
    json = record.as_json()
        
        
    