# Before you begin

Make sure you are on the master branch.

```
git checkout master
```

Pull lastest changes from upstream master branch.
```
git pull upstream master
```
**Note if you get an error you  may need to first add the upstream as a remote**
```
git remote add upstream https://github.com/UWICompSociety/fst_backend.git
```

Also incase there are any changes to the database. Run a migration  so your local database can be  updated.
```
python manage.py migrate
```

# Create a branch for your feature

Let us say you are working on the contacts feature then you would create a seperate branch for that feature.

```
git checkout -b contacts
```

This will create a new branch called contacts. You can verify this by using the following commanad.
```
git branch
```

# Commit code

You will then go ahead and write the code for your feature. After your  finished it is time to commit your changes to your local repository.
```
git add --all
git commit -m "A descritpive message of what you did for this feature"
```

# Write a unit test
Create a unit test for the feature you created in tests.py. Run the tests to make  sure  everything is ok.
```
python manage.py test
```
**Note if you get an error saying permission denied, it means you need to give the database user createdb permission.Run the  below command in postgres**.
```
ALTER ROLE fst_admin CREATEDB;
```

# Push  your code
You will go ahead and now push your branch
```
git push origin contacts
```

# Submit a pull request
Go to github and send a pull request. Once the pull request has been merged you can checkout to master again and pull the latest changes from  the upstream.
