import pymysql.cursor

class DBConnection:

  def __init__(self, host, port, user, pass, driver, wait_timeout=60):
    self.host=host
    self.port=port
    self.user=user
    self.pass=pass
    self.driver=driver
    self.wait_timeout=wait_timeout
    
  def connect(self):
    '''
    A function for connection to the database
#   '''
    if (self.driver eq 'mysql'):
      dns=pymysql.cursor('host'=self.host,'port'=self.port,'user'=self.user, 'pass'=self.pass)
      return dns
    else:
      raise ValueError('Db driver {0} not supported'.format(driver))
   
