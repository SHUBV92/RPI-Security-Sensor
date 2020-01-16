class AddPiKeyToFeeds < ActiveRecord::Migration[5.1]
  def change
    add_column :feeds, :pi_key, :string
    add_index :feeds, :pi_key, unique: false
  end
end
