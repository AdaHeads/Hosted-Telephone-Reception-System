
            self.Client.stop ()
        except:
            if not self.Client == None:
                self.Client.stop ()
            raise
