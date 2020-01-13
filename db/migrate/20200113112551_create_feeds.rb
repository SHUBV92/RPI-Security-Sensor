class CreateFeeds < ActiveRecord::Migration[5.1]
  def change
    create_table :feeds do |t|
      t.datetime :created_at
      t.string :image_string

      t.timestamps
    end
  end
end
