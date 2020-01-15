class AddPiKeyToUsers < ActiveRecord::Migration[5.1]
  def change
    add_column :users, :pi_key, :string
    add_index :users, :pi_key, unique: true
  end
end
