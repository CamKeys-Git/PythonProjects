class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
 
  def __repr__(self):
    return '%s. "%s." %s, %s. %s, %s.' % (self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location) 
  
class Marketplace:
  
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, old_listing):
    self.listings.remove(old_listing)
    
  def show_listings(self):
    for listing in  self.listings:
      print(listings)
  
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
    
  
    
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return '%s, %s.' % (self.art.title, self.price)
    
    
veneer = Marketplace()
    
edytta = Client('Edytta Halpirt', 'Private Collection', False)

girl_with_mandolin = Art("Picasso, Pablo", 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)
  
moma = Client('The MOMA', 'New York', True)    
    
print(girl_with_mandolin)    
    
    
    
    
    
    
    
    
